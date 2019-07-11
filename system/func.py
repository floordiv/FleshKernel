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
    except IndexError:
        return 'index-error'
    except FileNotFoundError:
        return 'file-not-found'
    except SyntaxError:
        return 'bad-syntax'
    except KeyboardInterrupt:
        return 'aborted'
    except Exception as running_function_exception:
        return str(running_function_exception)


def broadcast(text_type, text, fg_color='white', bg_color='black'):
    pass
