
<template>
    <div class="content">
      <div class="inner-content">
        <h2>Suche dir eine Übung aus!</h2>
        <div class="row">
          <div class="col">
        <RouterLink class="router-link" to="./zahlenlesen">
          <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
            <div class="card-header"></div>
            <div class="card-body">
              <h5 class="card-title">Zahlen lesen</h5>
              <p class="card-text">Lese die Zahlen und tippe sie ein</p>
            </div>
          </div>
        </RouterLink>
      </div>
      <div class="col">
        <RouterLink class="router-link" to="./plusrechnen">
          <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
            <div class="card-header"></div>
            <div class="card-body">
              <h5 class="card-title">Plus rechnen</h5>
              <p class="card-text">Hier kannst du zeigen, wie gut du plus rechnen kannst</p>
            </div>
          </div>
        </RouterLink>
      </div>
      </div>
      <div class="row">
        <div class="col">
        <RouterLink class="router-link" to="./minusrechnen">
          <div class="card text-bg-success mb-3" style="max-width: 18rem;">
            <div class="card-header"></div>
            <div class="card-body">
              <h5 class="card-title">Minus rechnen</h5>
              <p class="card-text">Dann zeig mal wie gut deine minus rechnen ist</p>
            </div>
          </div>
        </RouterLink>
      </div>
      <div class="col">
        <RouterLink class="router-link" to="./geschichtenlesen">
          <div class="card text-bg-warning mb-3" style="max-width: 18rem;">
            <div class="card-header"></div>
            <div class="card-body">
              <h5 class="card-title">Plus und minus rechnen</h5>
              <p class="card-text">Hier rechnen Profis. Plus und minus gemischt</p>
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
