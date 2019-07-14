from tornado.web import Application, RequestHandler, HTTPError
from tornado.ioloop import IOLoop
from py_block_ip import protect_attack


class NotFoundHandler(RequestHandler):
    def get(self, *args, **kwargs):

        blocked = protect_attack(ip=self.request.remote_ip, path=self.request.uri, file_rules='example_rules.txt')
        if blocked is False:
            raise HTTPError(
                status_code=404,
                reason=f"Ops not found resource you ip is {self.request.remote_ip}"
            )

class HomeHandler(RequestHandler):
    def get(self):
        self.write({'ok': 'ok'})


def make_app():
    urls = [
        ("/", HomeHandler),
        (r"(.*)", NotFoundHandler),
    ]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
