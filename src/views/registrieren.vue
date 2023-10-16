<template>

    <div>
        <h2>Registrierung</h2>
  
  
  <div>
    <form class="px-4 py-3">
      <div class="mb-3">
        <label  class="form-label">Benutzername</label>
        <input v-model="username" type="text" class="form-control" placeholder="Benutzername">
      </div>
      <div class="mb-3">
        <label for="exampleDropdownFormPassword1" class="form-label">Passwort</label>
        <input v-model="password" type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Passwort">
      </div>
      <div class="mb-3">
        <label for="exampleDropdownFormPassword1" class="form-label">Passwort wiederholen</label>
        <input v-model="confirmPassword" type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Passwort wiederholen">
      </div> 
      <div>
        <p>{{ incorrectPassword }}</p>
        <p>{{ message }}</p>
        <p>{{ regestrationStatus }}</p>
      </div>

      <button type="submit" class="btn btn-outline-info" @click="validPassword">Registrieren</button>
    </form>

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
        confirmPassword: '',
        incorrectPassword: '',
        message: '',
        regestrationStatus: '',
      };
    },
    methods: {
      async validPassword(event) {
        event.preventDefault();
        if (this.password.length < 8) {
          alert("Das Passwort muss mindestens 8 Zeichen lang sein!")
          return false;
        }
        if (!/[A-Z]/.test(this.password)) {
          alert("Du musst mindestens einen Grossbuchstaben verwenden!")
          return false;
        }
        if (!/[!@#$%^&*()-,.?":{}|<>]/.test(this.password)) {
          alert("Du must min. ein Sonderzeichen benutzen!")
          return false;
        }
        if(!/\d/.test(this.password)) {
          alert("Es muss mindestens eine Zahl enthalten sein!")
          return false;
        }
        await this.addUser(event); 
        return true;

      },

      async addUser(event) {
        event.preventDefault();
        if (this.password !== this.confirmPassword) {
          alert("Die Passwörter stimmen nicht überein!")
           return;
        }
        else {
        try {
          const response = await axios.post('http://127.0.0.1:5000/add_user', {
            username: this.username,
            password: this.password,
          });
          console.log(response.data.message + "Frontend")
          
          if (response.data.message === 'Die Registrierung war erfolgreich') {
            alert(this.message = response.data.message + " Du kannst dich jetzt anmelden!")
            this.$router.push({ name: 'login' });
        } 
          if(response.data.messageUser === "Der Benutzername ist schon vorhanden") {
            alert(this.message = response.data.messageUser) 
          }
        else {
          this.message = 'Anmeldung fehlgeschlagen';
        }
        } catch (error) {
          console.error(error);
        }      
      }
      },
    },

  
  };
  </script>

