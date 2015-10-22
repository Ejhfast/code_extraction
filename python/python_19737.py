# python tcp server sending data to multiple clients
for i in clients:
          if i is not s:
            i.send(data)
