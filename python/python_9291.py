# How can i get id of cascade deleted (or marked for delete) items in sqlalchemy?
create trigger example_tcn_trigger
  after delete on example
  for each row execute procedure triggered_change_notification();
