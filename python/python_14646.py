# Django tries to add a null value in id (primary key) field
ALTER TABLE imageset_image ALTER COLUMN id SET DEFAULT nextval('imageset_image_id_seq'::regclass);
