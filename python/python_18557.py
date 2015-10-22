# get large number of Post values
def post(self):
    var_dump({ k: self.get_argument(k) for k in self.request.arguments })
