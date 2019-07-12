import settings
import text


class current:
    def time(self):
        import datetime
        try:
            return str(datetime.datetime.today()).split('.')[0].split()[1]
        except:
            return None

    def date(self):
        import datetime
        try:
            return str(datetime.datetime.today()).split('.')[0].split()[0]
        except:
            return None


def sfcall(func, *args):    # safe function call
    try:
        exec(f'{func}{args})')
    except Exception as running_func_exception:
        return str(type(running_func_exception))


def broadcast(text_type, text, fg_color='white', bg_color='black'):
    if settings.broadcast.allow:
        curr_time = current.time(0) if settings.broadcast.show_time else None
        curr_date = current.time(0) if settings.broadcast.show_date else None
        text_type = text_type if settings.broadcast.show_type else None
        if text_type in settings.broadcast.types:
            line = f'[{text.output(str(text_type).upper(), fg_color=settings.broadcast.types[str(text_type).lower()][0], bg_color=settings.broadcast.types[str(text_type).lower()][1], end="")}] [{curr_date} {curr_time}]' \
                f' {text}'
            print(line)
        else:
            print(f'[{text.output(text_type.upper(), fg_color=fg_color, bg_color=bg_color, end="")}] [{curr_date} {curr_time}] {text}')
