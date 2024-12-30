# Steps to deploy application
1. ```git clone https://github.com/arciol/dcfilmweb-changed.git```
2. ```cd dcfilmweb-changed```
3. ```docker build -t zit-projekt .```
4. ```docker run -d -p 8000:8000 zit-projekt```
5. Go to your browser under localhost:8000 address

## Important !!!
Due to my university project application has Stored XSS vulnerability implemented, be careful using it for your own purposes.
