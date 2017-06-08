eval_compiled = {}

def eval_filter(code, **kwargs):
    try:
        c = eval_compiled[code]
    except KeyError:
        c = compile(code, '<eval_filter>', 'eval')
        eval_compiled[code] = c

    result = eval(c, {}, kwargs)
    return result


class FilterModule(object):
    def filters(self):
        return {
            'eval': eval_filter,
        }
