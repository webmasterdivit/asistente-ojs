# Dockerfile para frontend Vue.js
FROM node:20-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Etapa de test (opcional)
FROM build-stage as test-stage
CMD ["npm", "run", "test"]

FROM nginx:alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
