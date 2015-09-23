from {{project}}.views import *
import logging
logger = logging.getLogger("app.views.main")

@app.route('/', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
#@is_logged_in
def main_page():
  page_data = get_page_data("dashboard")
  return render_template('dashboard.html', page_data=page_data)

