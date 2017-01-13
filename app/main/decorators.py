from functools import wraps
from flask.ext.login import current_user
from flask import abort

def required_roles(role_id):
   def wrapper(f):
      @wraps(f)
      def wrapped(*args, **kwargs):
         if get_current_user_role() != role_id:
            abort(403)
         return f(*args, **kwargs)
      return wrapped
   return wrapper
 
def get_current_user_role():
   return current_user.role_id