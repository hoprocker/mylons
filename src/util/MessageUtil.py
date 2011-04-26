from flask import g,get_flashed_messages,flash,_request_ctx_stack,session
import pickle

ERROR_KEY = "_error"
MSG_KEY = "_msg"

def addError(msg):
    """
    setup to add error msg for next request
    """
    _add_msg_for_key(msg, ERROR_KEY)

def addMessage(msg):
    """
    setup to add msg for next request
    """
    _add_msg_for_key(msg, MSG_KEY)

def getErrors():
    """
    get errors from the previous request
    """
    return _get_from_prev_flash(ERROR_KEY)

def getMessages():
    """
    get messages from the previous request
    """
    return _get_from_prev_flash(MSG_KEY)

def hasErrors():
    """
    check if the current request has any errors
    """
    errors = _get_cur_flashed_val(ERROR_KEY)
    return len(errors) > 0

## helpers

def _add_msg_for_key(msg, key):
    msgs = _get_cur_flashed_val(key)
    msgs.append(msg)
    flash(pickle.dumps(msgs), key)

def _get_cur_flashed_val(key):
    """
    helper to pull values flashed in current session
    """
    if session.has_key('_flashes'):
        errors = filter(lambda(x): x[0] == key, session['_flashes'])
        if len(errors) > 0:
            return pickle.loads(errors[0][1])
    return []

def _get_from_prev_flash(key):
    """
    pull previously flashed/pickled values
    """
    msgs = filter(lambda(x): x[0] == key, get_flashed_messages(True))
    if len(msgs) < 1:
        return None
    return pickle.loads(msgs[0][1])



