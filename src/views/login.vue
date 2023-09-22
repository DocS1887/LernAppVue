<template>
  <div>
    <h1>Registrierung</h1>
    <form @submit.prevent="register">
      <label for="username">Benutzername: </label>
      <input type="text" id="username" v-model="username" required>
      <br>
      <label for="password">Passwort: </label>
      <input type="password" id="password" v-model="password" required>
      <br>
      <button type="submit">Registrieren</button>
      </form>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    register() {
      const accessToken = 'Ihr_Autorisierungs-Token'; // Hier setzen Sie Ihren Token

      axios.post('http://localhost:8889/register', {
        username: this.username, // Verwenden Sie die eingegebenen Daten
        password: this.password, // Verwenden Sie die eingegebenen Daten
      }, {
        headers: {
          'Authorization': `Bearer ${accessToken}`, // Verwenden Sie den Token in Ihrem Header
        },
      })
      .then(response => {
        // Erfolgreiche Antwort verarbeiten
        console.log(response.data);
      })
      .catch(error => {
        // Fehler verarbeiten
        console.error(error);
      });
    },
  },

}
</script>
