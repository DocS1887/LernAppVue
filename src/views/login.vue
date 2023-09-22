<template>

  <div>
    <h1>Anmeldung</h1>


<div>
  <form class="px-4 py-3">
    <div class="mb-3">
      <label  class="form-label">Benutzername</label>
      <input v-model="username" type="text" class="form-control" id="exampleDropdownFormEmail1" placeholder="Benutzername">
    </div>
    <div class="mb-3">
      <label for="exampleDropdownFormPassword1" class="form-label">Passwort</label>
      <input v-model="password" type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Passwort">
    </div>
    
    <div class="mb-3">
      <div class="form-check">
        <input type="checkbox" class="form-check-input" id="dropdownCheck">
        <label class="form-check-label" for="dropdownCheck">
          angemeldet bleiben
        </label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary" @click="addUser">Anmelden</button>
  </form>
  <div class="dropdown-divider"></div>
  <a class="dropdown-item" href="#">Neu hier? Melde dich an!</a>
  <a class="dropdown-item" href="#">Passwort vergessen?</a>
</div>
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
    async addUser() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/add_user', {
          username: this.username,
          password: this.password,
        });
        console.log(response.data.message);
      } catch (error) {
        console.error(error);
      }
    },
  },

};
</script>
