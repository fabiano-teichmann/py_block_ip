from tornado.web import Application, RequestHandler, HTTPError
from tornado.ioloop import IOLoop
from py_block_ip import protect_attack


class NotFoundHandler(RequestHandler):
    def get(self, *args, **kwargs):

        blocked = protect_attack(ip=self.request.remote_ip,
                                 path=self.request.uri,
                                 file_rules='app/example_rules.txt',
                                 ip_accept=['127.0.0.1'],
                                 subnet='0/24')
        if blocked is False:
            raise HTTPError(
                status_code=404,
                reason=f"Ops not found resource and you ip is {self.request.remote_ip}"
            )
        else:
            raise HTTPError(
                status_code=423,
                reason=f"Access deny. Your ip {self.request.remote_ip} was blocked "
            )

class HomeHandler(RequestHandler):
    def get(self):
        self.write({'message': 'Hello you app example Pyblock is run success.'})


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
