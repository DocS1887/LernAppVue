<template>
  <div class="row" style="padding-top: 3%">
    <div class="col">
    <aside>
      <p><strong>Hallo und willkommen</strong>
      bei Lernen macht Spaß</p>
      <p>Melde dich an um Punkte zu sammeln. Mit diesen Punkten kannst du dann ein Spiel spielen.</p>
      <p>Hier geht es zur Anmeldung <br>
        <p>
      <RouterLink to="./login">
      <button type="button" class="btn btn-outline-select">Anmeldung</button>
      </RouterLink>
    </p>
      </p>
    </aside>
  </div>
  <div class="col">
    <main>
    <section>
      <div class="col d-flex justify-content-end">
        <RouterLink to="./lesen">
        <div class="card">
            <div class="card-body d-flex flex-column align-items-center">
                <h5 class="card-title">Deutsch</h5>
                <p class="card-text">Ob Buchstaben, Wörter und ganze Texte. Bald kannst du alles lesen :)</p>
            </div>
        </div>
        </RouterLink>
      </div>
    </section>
    <section>
      <div class="col d-flex justify-conten-start">
        <RouterLink to="./rechnen">
        <div class="card">
            <div class="card-body d-flex flex-column align-items-center">
                <h5 class="card-title">Mathe</h5>
                <p class="card-text">Plus und Minus sind für dich bald kein Problem mehr!</p>
            </div>
        </div>
        </RouterLink>
      </div>
    </section>
    </main>
  </div>
  </div>
</template>

<style scoped>

.card {
    border-radius: 1rem;
    width: 22rem;
    text-align: center;
    padding: 2%;
    box-shadow: 0 0 10px black;
    border: 1px solid;
}

.card:hover {
              box-shadow: 0 1.9rem 3.8rem rgba(0, 0, 0, 0.3), 0 1.5rem 1.2rem rgba(0, 0, 0, 0.22);
              transform: translate(0, -1rem);
              transition-delay: 150ms;
            }

a:link {
    text-decoration: none;
}
section {
    padding: 5%;
}
aside {
  border: 1px solid;
  box-shadow: 0 0 10px black;
  padding: 2%;
  min-height: 22rem;
  text-align: center;
  padding-top: 4rem;
}

</style>

<script setup>
</script>
