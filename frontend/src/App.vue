<template>
  <div id="app">
    <h1>Consultas OJS con OpenAI</h1>
    <form @submit.prevent="sendQuery">
      <textarea v-model="query" placeholder="Escribe tu consulta sobre OJS"></textarea>
      <button type="submit">Enviar</button>
    </form>
    <div v-if="response">
      <h2>Respuesta:</h2>
      <pre>{{ response }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const query = ref('')
const response = ref('')

const sendQuery = async () => {
  const res = await axios.post('http://localhost:8000/ask', { query: query.value })
  response.value = res.data.response
}
</script>

<style>
#app { max-width: 600px; margin: 2rem auto; font-family: sans-serif; }
textarea { width: 100%; min-height: 100px; }
button { margin-top: 1rem; }
</style>
