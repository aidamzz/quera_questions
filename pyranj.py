from logger import logger

PREFIX = 'prefix'
FUNC = 'func'
RUN = 'run'

def pyranj_message(e, prefix=None):
    if prefix is None:
        prefix = '[EXCEPTION]'
    return f'{prefix} :: {e}'

def pyranj_decorator(prefix=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                logger.log(pyranj_message(e, prefix))

        return wrapper

    return decorator


def get_pyranj(prefix_=None):
    class InnerPyRanjMeta(type):
        def __call__(cls, *args, **kwargs):
            if cls != InnerPyRanj:
                return super(InnerPyRanjMeta, cls).__call__(*args, **kwargs)
            param = args[0] if args else None
            func = param if type(param) == type(pyranj_decorator) else None
            prefix = kwargs.get(PREFIX, None)
            if func:
                return pyranj_decorator(prefix_)(func)
            return get_pyranj(prefix)

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                logger.log(pyranj_message(exc_val, prefix=prefix_))
            return True

    class InnerPyRanj(metaclass=InnerPyRanjMeta):
        def __getattribute__(self, item):
            attr = super().__getattribute__(item)
            if item == RUN:
                return pyranj_decorator(prefix_)(attr)
            return attr

    return InnerPyRanj
PyRanj = get_pyranj()