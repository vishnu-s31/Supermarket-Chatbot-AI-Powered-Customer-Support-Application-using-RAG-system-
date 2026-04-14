CREATE DATABASE IF NOT EXISTS Supermarket;
USE Supermarket;

CREATE TABLE IF NOT EXISTS Product_details (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10, 2),
    in_stock BOOLEAN,
    stock_quantity INT,
    description TEXT
);

INSERT INTO Product_details (name, category, brand, price, in_stock, stock_quantity, description) VALUES
-- Snacks
('Lays Classic Salted Chips 100g', 'Snacks', 'Lays', 20.00, TRUE, 50, 'Crispy potato chips with classic salted flavor.'),
('Kurkure Masala Munch 80g', 'Snacks', 'Kurkure', 15.00, TRUE, 40, 'Spicy, crunchy corn puffs.'),
('Hide & Seek Fab Chocolate 120g', 'Snacks', 'Parle', 30.00, TRUE, 25, 'Chocolate cream filled biscuits.'),
('Unibic Cashew Cookies 150g', 'Snacks', 'Unibic', 45.00, TRUE, 20, 'Crunchy cashew cookies rich in taste.'),
('Perk Chocolate 30g', 'Snacks', 'Cadbury', 10.00, TRUE, 100, 'Layered wafer chocolate bar.'),

-- Home Needs
('Surf Excel Detergent Powder 1kg', 'Home Needs', 'Surf Excel', 120.00, TRUE, 35, 'Effective stain remover detergent.'),
('Harpic Toilet Cleaner 500ml', 'Home Needs', 'Harpic', 65.00, TRUE, 60, 'Kills 99.9% germs. Tough on stains.'),
('Lizol Floor Cleaner Citrus 975ml', 'Home Needs', 'Lizol', 145.00, TRUE, 30, 'Kills germs and leaves fresh citrus fragrance.'),
('Dettol Hand Wash 200ml', 'Home Needs', 'Dettol', 60.00, TRUE, 45, 'Antibacterial liquid hand wash.'),
('Godrej Aer Room Freshener 240ml', 'Home Needs', 'Godrej', 99.00, TRUE, 28, 'Air freshener with long-lasting fragrance.'),

-- Makeup & Beauty
('Lakme Facewash 100ml', 'Makeup & Beauty', 'Lakme', 160.00, TRUE, 30, 'Daily face wash for glowing skin.'),
('Maybelline Colossal Kajal', 'Makeup & Beauty', 'Maybelline', 180.00, TRUE, 25, '12-hour smudge-proof eye kajal.'),
('Ponds BB Cream 30g', 'Makeup & Beauty', 'Ponds', 125.00, TRUE, 15, 'BB cream for instant glow.'),
('Himalaya Lip Balm 10g', 'Makeup & Beauty', 'Himalaya', 35.00, TRUE, 50, 'Protects lips from dryness.'),
('Lakme Compact Powder 9g', 'Makeup & Beauty', 'Lakme', 150.00, TRUE, 22, 'Matte finish compact powder.'),

-- Beverages
('Pepsi 750ml', 'Beverages', 'PepsiCo', 40.00, TRUE, 70, 'Refreshing cola drink.'),
('Appy Fizz 250ml', 'Beverages', 'Parle Agro', 25.00, TRUE, 65, 'Sparkling apple drink.'),
('Real Orange Juice 1L', 'Beverages', 'Dabur', 95.00, TRUE, 32, 'No added preservative fruit juice.'),
('Red Bull Energy Drink 250ml', 'Beverages', 'Red Bull', 110.00, TRUE, 18, 'Energy drink for alertness and focus.'),
('Amul Kool Badam 200ml', 'Beverages', 'Amul', 25.00, TRUE, 40, 'Flavored milk drink with almond.'),

-- Fruits & Vegetables
('Apple (1kg)', 'Fruits & Vegetables', 'Fresh Farm', 120.00, TRUE, 60, 'Fresh, juicy red apples.'),
('Tomato (1kg)', 'Fruits & Vegetables', 'Local', 35.00, TRUE, 80, 'Farm fresh ripe tomatoes.'),
('Banana (1 dozen)', 'Fruits & Vegetables', 'Fresh Farm', 50.00, TRUE, 90, 'Sweet and healthy bananas.'),
('Carrot (1kg)', 'Fruits & Vegetables', 'Local', 40.00, TRUE, 70, 'Rich in vitamin A. Good for eyesight.'),
('Spinach (1 bunch)', 'Fruits & Vegetables', 'Local', 15.00, TRUE, 100, 'Green leafy vegetable. Rich in iron.'),

-- Dairy
('Amul Butter 500g', 'Dairy', 'Amul', 235.00, TRUE, 33, 'Pasteurized butter made from cream.'),
('Mother Dairy Milk 1L', 'Dairy', 'Mother Dairy', 56.00, TRUE, 50, 'Toned milk.'),
('Britannia Cheese Slices (10 pcs)', 'Dairy', 'Britannia', 85.00, TRUE, 30, 'Processed cheese slices.'),
('Nestle Yogurt Strawberry 100g', 'Dairy', 'Nestle', 25.00, TRUE, 20, 'Flavored yogurt cup.'),
('Amul Paneer 200g', 'Dairy', 'Amul', 80.00, TRUE, 25, 'Soft, fresh paneer block.'),

-- Baby Products
('Johnson Baby Powder 100g', 'Baby Products', 'Johnson & Johnson', 55.00, TRUE, 20, 'Gentle baby powder.'),
('Pampers Diapers M (20 pcs)', 'Baby Products', 'Pampers', 399.00, TRUE, 15, 'Comfortable and dry diapers.'),
('Cerelac Wheat Apple 300g', 'Baby Products', 'Nestle', 175.00, TRUE, 18, 'Infant cereal with fruit.'),
('Himalaya Baby Lotion 200ml', 'Baby Products', 'Himalaya', 120.00, TRUE, 22, 'Moisturizing lotion for babies.'),
('Mee Mee Baby Wipes (72 pcs)', 'Baby Products', 'Mee Mee', 99.00, TRUE, 28, 'Soft and thick wipes.'),

-- Cleaning Supplies
('Vim Dishwash Bar 500g', 'Cleaning Supplies', 'Vim', 25.00, TRUE, 90, 'Removes grease effectively.'),
('Colin Glass Cleaner 500ml', 'Cleaning Supplies', 'Colin', 85.00, TRUE, 34, 'Streak-free shine for glass.'),
('Scotch-Brite Scrub Pad', 'Cleaning Supplies', 'Scotch-Brite', 10.00, TRUE, 120, 'Removes tough stains.'),
('Domex Toilet Cleaner 500ml', 'Cleaning Supplies', 'Domex', 78.00, TRUE, 29, 'Kills germs and keeps toilet fresh.'),
('Exo Dishwash Liquid 250ml', 'Cleaning Supplies', 'Exo', 45.00, TRUE, 45, 'Gentle on hands, tough on grease.');
