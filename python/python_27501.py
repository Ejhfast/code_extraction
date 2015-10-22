# Improve SQL statement with Index Scan Backward
CREATE INDEX idx_order_messages on mail_message (id) where model = 'purchase.order'
