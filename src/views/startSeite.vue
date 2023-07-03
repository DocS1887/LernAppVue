<template>
    <div class="content">
        <div class="inner-content">
            <div class="row">
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <img src="../assets/img/lesen.png" class="card-img-top" alt="...">
                        <div class="card-body d-flex flex-column align-items-center">
                            <h5 class="card-title">Deutsch</h5>
                            <p class="card-text">Ob Buchstaben, Wörter und ganze Texte. Bald kannst du alles lesen :)</p>
                            <RouterLink to="./lesen"><a class="btn btn-warning mx-auto">Los geht's mit Deutsch</a></RouterLink>
                        </div> 
                    </div>
                </div>
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <img src="../assets/img/rechnen.jpg" class="card-img-top" style="width: 250px; height: 350px;">
                        <div class="card-body d-flex flex-column align-items-center">
                            <h5 class="card-title">Mathe</h5>
                            <p class="card-text">Plus und Minus sind für dich bald kein Problem mehr!</p>
                            <a href="#" class="btn btn-warning mx-auto">Los geht's mit Mathe</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
h1 {
    text-align: center;
    margin-bottom: 2rem;
    font-family: Bubblegum;
}

</style>