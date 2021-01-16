from flask import render_template, session, url_for, redirect
from app import APP
from app.errors import NotFoundException
from app.logging import LOGGER
import traceback


@APP.route("/something_went_wrong")
def handle_generic_error():
    """Handle generic errors"""
    message = str(session.pop("runtimeException",
                              "Sorry, something went wrong"))
    LOGGER.warning(message)
    return render_template("error.html", message=message)


@APP.errorhandler(NotFoundException)
@APP.errorhandler(Exception)
def error_request_director(error):
    """Redirect all errors to their handler to prevent double submits"""
    if (isinstance(error, NotFoundException)):
        session["runtimeException"] = str(error)
        return redirect(url_for("handle_generic_error"))
    else:
        # probably should look into this
        LOGGER.error("Unhandled exception")
        LOGGER.error(error)
        traceback.print_exc()
        return redirect(url_for("handle_generic_error"))
