from {{project}}.views import *
import logging
logger = logging.getLogger("app.views.main")

@app.route('/', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
#@is_logged_in
def main_page():
  g.page = 'dashboard'
  return render_template('dashboard.html')
