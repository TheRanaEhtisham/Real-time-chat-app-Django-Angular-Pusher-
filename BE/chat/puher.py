import pusher

pusher_client = pusher.Pusher(
  app_id='1973911',
  key='---',
  secret='--',
  cluster='ap2',
  ssl=True
)

# pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})