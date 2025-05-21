# use node js. image
FROM node:18

WORKDIR /app


COPY package*.json ./
RUN npm install


COPY . .

EXPOSE 500

CMD ["node" , "index.js"]

### Created by pranav