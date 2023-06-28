FROM node:16
# Working directory of our container
WORKDIR /app
# /app
COPY package.json .
RUN npm install
COPY . ./
EXPOSE 3000
# Run the container
CMD ["node" , "index.js"]