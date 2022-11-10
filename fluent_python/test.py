def tag(name, *args, cls = None, **kwargs):
    if cls is not None:
        kwargs['class'] = cls
    if kwargs:
        kwargs_str = ''.join('%s="%s"' % (attr, value) for attr, value in sorted(kwargs.items()))

    else:
        kwargs_str = ''

    if args:
        return '\n'.join('<%s%s>%s</%s>' % (name, kwargs_str, c, name) for c in args)
    else:
        return '<%s%s />' % (name, kwargs_str)

print(tag('br', 'hello'))
