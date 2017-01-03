from functools import wraps
from flask import redirect, url_for, flash
from flask.ext.login import current_user

def required_roles(role_id):
   def wrapper(f):
      @wraps(f)
      def wrapped(*args, **kwargs):
         if get_current_user_role() != role_id:
            flash('sorry not allowed to access')
            return redirect(url_for('home_page'))
         return f(*args, **kwargs)
      return wrapped
   return wrapper
 
def get_current_user_role():
   return current_user.role_id