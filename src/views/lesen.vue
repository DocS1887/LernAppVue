
<template>
<div class="content">
  <div class="inner-content">
    <h2>Suche dir eine Übung aus!</h2>
    <div class="row">
      <div class="col">
    <RouterLink class="router-link" to="./buchstabenlesen">
      <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
        <div class="card-header"></div>
        <div class="card-body">
          <h5 class="card-title">Buchstaben lesen</h5>
          <p class="card-text">Hier kannst du die einzelnen Buchstaben lernen</p>
        </div>
      </div>
    </RouterLink>
  </div>
  <div class="col">
    <RouterLink class="router-link" to="./woerterlesen">
      <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
        <div class="card-header"></div>
        <div class="card-body">
          <h5 class="card-title">Wörter lesen</h5>
          <p class="card-text">Buchstaben kennst du alle? Gut. Probiere es mit ganzen Wörtern</p>
        </div>
      </div>
    </RouterLink>
  </div>
  </div>
  <div class="row">
    <div class="col">
    <RouterLink class="router-link" to="./leseteppich">
      <div class="card text-bg-success mb-3" style="max-width: 18rem;">
        <div class="card-header"></div>
        <div class="card-body">
          <h5 class="card-title">Lesetepich</h5>
          <p class="card-text">Die guten alten Leseteppiche aus der Schule. Alle da ;)</p>
        </div>
      </div>
    </RouterLink>
  </div>
  <div class="col">
    <RouterLink class="router-link" to="./geschichtenlesen">
      <div class="card text-bg-warning mb-3" style="max-width: 18rem;">
        <div class="card-header"></div>
        <div class="card-body">
          <h5 class="card-title">Geschichten lesen</h5>
          <p class="card-text">Buchstaben und Wörter sind für Anfänger? Gut, dann lese kleine Geschichten.</p>
        </div>
      </div>
    </RouterLink>
  </div>
  </div>
</div>
</div>
</template>



<style scoped>
.router-link {
  text-decoration: none;
  padding: 5%;
}
h2 {
  text-align: center;
  padding-bottom: 2%;
}
.card-body {
  height: 10rem;
}

</style>