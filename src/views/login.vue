<template>
  <div>
    <h2>Anmeldung</h2>
    <div>
      <form class="px-4 py-3" @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">Benutzername</label>
          <input v-model="username" type="text" class="form-control" placeholder="Benutzername" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Passwort</label>
          <input v-model="password" type="password" class="form-control" placeholder="Passwort" required>
        </div>
        <div class="mb-3">
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="dropdownCheck">
            <label class="form-check-label" for="dropdownCheck">
              angemeldet bleiben
            </label>
          </div>
        </div>
        <button type="submit" class="btn btn-outline-info">Anmelden</button>
      </form>
      <div class="dropdown-divider"></div>
      <a class="dropdown-item"><RouterLink to="/registrieren">Neu hier? Melde dich an!</RouterLink></a>
      <a class="dropdown-item" href="#">Passwort vergessen?</a>
    </div>
    <div v-if="message" class="alert alert-danger mt-3">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/login', {
          username: this.username,
          password: this.password,
        });


        const token = response.data.token
        if (response.data.message === 'Erfolgreich eingeloggt' ) {
          localStorage.setItem('authToken', token)
          window.location.reload();
          this.$router.push({ name: 'Testung' });
        } else {
          this.message = 'Anmeldung fehlgeschlagen';
        }
      } catch (error) {
        console.error(error);
        this.message = 'Ein Fehler ist aufgetreten';
      }
    },
  },
};
</script>

