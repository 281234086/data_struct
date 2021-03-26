import json
import psycopg2

import os
import time
from datetime import datetime
from datetime import timedelta

import logging.handlers
import logging


LOG_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "logs/purchase_sku"

class Logger(object):
    def __init__(self):
        self.log_name = LOG_DIRECTORY + "/" + time.strftime("%Y_%m_%d") + '.log'
        self.format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        # 实例化logger对象
        self._logger = logging.getLogger()
        # 指定日志输出格式
        if not self._logger.handlers:
            self.formatter = logging.Formatter(fmt=self.format, datefmt=self.datefmt)
            # 给logger添加文件日志处理器
            self._logger.addHandler(self.get_file_handler(self.log_name))
            # 指定日志的最低输出级别，因为nsq也会输出info级别的日志，导致多余log，提高日志输出等级屏蔽nsq日志
            self._logger.setLevel(logging.INFO)

    def get_file_handler(self, log_name):
        # 文件处理器
        # 日志名字
        fh = logging.handlers.TimedRotatingFileHandler(
            log_name, 'midnight', 1, 0)
        # fh.suffix = '%Y%m%d'
        # 指定log的输出形式，通过控制台的setFormatter方法来实现
        fh.setFormatter(self.formatter)
        return fh

    @property
    def getlog(self):
        return self._logger


logger = Logger().getlog



def update_purchase_sku_return():
    conn = psycopg2.connect(database="starmerx", user="wenhuang", password="Wen2012", host="192.168.1.187",
                               port="5432")
    cr_pg = conn.cursor()


    conn_pg = psycopg2.connect(database="starmerx", user="wenhuang", password="Wen2012", host="192.168.1.90",port="5432")
    cursor_pg = conn_pg.cursor()
    logger.info('=======Start=======')

    del_table = """
delete from purchase_sku_return where 1 = 1;
    """
    logger.info(del_table)
    cursor_pg.execute(del_table)
    conn_pg.commit()


    pg_select_sql = """
    select sm.product_id,max(pp.default_code),max(sm.name), sum(sm.product_qty) from
stock_move sm, stock_picking sp, product_product pp
where sm.picking_id=sp.id and sm.state='confirmed' and pp.id=sm.product_id and sp.type='out' and sp.location_id in (193, 182) group by sm.product_id;
       """

    cr_pg.execute(pg_select_sql)

    result_pg = cr_pg.fetchall()
    no_use_sku = []
    no_partner_sku = []
    count = 0
    try:
        for result in result_pg:
            product_id = result[0]
            sku_name = result[1]
            product_name = str(result[2]).replace("'", "_")
            shortage_qty = result[3]
            # 供应商name
            partner_sql = """
            SELECT name from product_supplierinfo where  product_id = (SELECT product_tmpl_id from  product_product where id = {}) and  sequence <> 20 ORDER BY "sequence" , id DESC;
            """.format(product_id)
            start = time.time()
            # print(partner_sql)
            cr_pg.execute(partner_sql)
            partner_res = cr_pg.fetchone()
            end = time.time()
            logger.info('查找供应商执行的时间为: %s' % (end-start))
            if not partner_res:
                no_partner_sku.append(sku_name)
                continue
            partner_id = partner_res[0]
            # 查找PO最早创建时间和采购员
            po_select_sql = """
            select po.most_early_create_date, po.purchaser_id from purchase_order_line pol left join purchase_order po on
            pol.order_id = po.id where pol.product_id= {} and (po.state in ('draft', 'purchasing', 'purchase_success')
            or (po.state='approved' and po.stock_state in ('assigned', 'receiving', 'partial', 'abnormal')))
            order by po.most_early_create_date desc;
            """.format(product_id)

            # print('查询po信息:', po_select_sql)
            start = time.time()

            cr_pg.execute(po_select_sql)
            po_msg = cr_pg.fetchone()
            end = time.time()
            logger.info('查找po_msg执行的时间为: %s' % (end-start))
            if not po_msg:
                no_use_sku.append(sku_name)
                continue
            po_early_create_date = po_msg[0]
            purchaser_id = po_msg[1]

            shortage_date = (datetime.now()- po_early_create_date).days
            # 查找能否回货
            now_time = datetime.now()
            # fifteen_days = now_time - timedelta(days=15)
            seven_days = now_time - timedelta(days=7)
            return_ok = False
            huihuo_sql ="""
    select * from starmerx_inventory_log where type = 'stock_in' and location_id in (182, 193) and product_id = {} and create_date>'{}' order by id desc
            """.format(product_id, seven_days)
            cr_pg.execute(huihuo_sql)
            huihuo_res = cr_pg.fetchone()
            if huihuo_res:
                return_ok = True
            # else:
            #     seven_days = now_time - timedelta(days=7)
            #     approved_sql = """
            #     select po.name from purchase_order_line pol left join purchase_order po on
            #     pol.order_id = po.id where pol.product_id= {} and po.state='approved' and po.date_approve>'{}' and po.date_approve <'{}'
            #     """.format(product_id, seven_days, now_time)
            #     cr_pg.execute(approved_sql)
            #     approved_res = cr_pg.fetchone()
            #     if approved_res:
            #         return_ok = True

            # 当天入库数量
            before_day = datetime.now() - timedelta(days=1)
            after_day = datetime.now()
            stockin_qty_sql = """
            select change_qty from starmerx_inventory_log where type = 'stock_in' and location_id in (182, 193) and product_id = {} and create_date > '{} 16:00:00' and create_date< '{} 16:00:00';
            """.format(product_id, str(before_day)[:10], str(after_day)[:10])
            cr_pg.execute(stockin_qty_sql)
            stockin_qty_res = cr_pg.fetchall()
            stockin_qty = 0
            for _stockin_qty in stockin_qty_res:
                stockin_qty += _stockin_qty[0]
            utc_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            insert_sql_mysql = """insert into purchase_sku_return (sku, product_name, product_id, update_date, purchaser_id,partner_id,shortage_date,po_early_create_date, shortage_qty, return_ok, stockin_qty, write_date, create_date, write_uid) values ('{}','{}',{}, '{}',{},{}, '{}', '{}', {}, '{}', {}, '{}', '{}', {});"""
            insert_sql_mysql = insert_sql_mysql.format(sku_name, product_name, product_id, utc_time,purchaser_id, partner_id, shortage_date,
                                                       po_early_create_date, shortage_qty, return_ok, stockin_qty, utc_time, utc_time, 1)
            logger.info(insert_sql_mysql)
            logger.info(count)
            count +=1
            cursor_pg.execute(insert_sql_mysql)

            # cr_pg.execute(insert_sql_mysql)
            conn.commit()  #commit主动关闭事物
            conn_pg.commit()

        logger.info('无PO单的sku: %s' % no_use_sku)
        logger.info('无供应商的sku: %s' % no_partner_sku)
        logger.info('共有%s缺货sku' % count)
        cr_pg.close()
        conn.close()
        cursor_pg.close()
        conn_pg.close()
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('错误 %s' % traceback.format_exc())
        conn_pg.rollback()
        cr_pg.close()
        conn.close()

        cursor_pg.close()
        conn_pg.close()


if __name__ == '__main__':
    """
    获取缺货sku
    """
    start = time.time()
    result = update_purchase_sku_return()
    end = time.time()
    logger.info('执行总时间: %s' %(end-start))