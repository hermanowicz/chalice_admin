from chalice import Chalice
from chalice import Rate
from chalice import Cron
import pendulum


app = Chalice(app_name='admin_jobs')


@app.schedule(Rate(1, Rate.MINUTES))
def first_function(event):
    w_now = pendulum.now("Europe/Warsaw")
    app.log.info(f"Running hello, world number 1 at {w_now.to_rfc3339_string()} of Warsaw time")
    return {'hello': 'world'}


@app.schedule(Rate(1, Rate.MINUTES))
def second_function(event):
    w_now = pendulum.now("Europe/Warsaw")
    app.log.info(f"Running hello, world number 2 at {w_now.to_rfc3339_string()} of Warsaw time")
    return {'hello': 'world2'}


@app.schedule(Cron('0/2', '*', '*', '*', '?', '*'))
def third_function(event):
    w_now = pendulum.now("Europe/Warsaw")
    app.log.info(f"Running hello, world number 3 at {w_now.to_rfc3339_string()} of Warsaw time")
    return {'hello': 'world2'}