<template>
  <h2>Der Leseteppich</h2>
  <div class="row">
    <nav class="navbar">
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('a')">a</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('b')">b</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('c')">c</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('d')">d</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('e')">e</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('f')">f</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('g')">g</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('h')">h</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('i')">i</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('j')">j</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('k')">k</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('l')">l</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('m')">m</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('n')">n</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('o')">o</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('p')">p</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('q')">q</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('r')">r</a>
    </nav>
  </div>
  <div class="row">
  <nav class="navbar">
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('s')">s</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('sch')">sch</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('st')">st</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('t')">t</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('u')">u</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('v')">v</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('w')">w</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('x')">x</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('y')">y</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('z')">z</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('ä')">ä</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('ö')">ö</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('ü')">ü</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('ei')">ei</a>
      <a class="navbar-brand" href="#" @click="ausgabeTeppich('eu')">eu</a>
    </nav>
    <div class="tabellenformat">
      <table>
        <tr v-for="(wort, index) in test" :key="index">
          <td v-if="test[index * 3]">{{ test[index * 3] }}</td>
          <td v-if="test[index * 3 + 1]">{{ test[index * 3 + 1] }}</td>
          <td v-if="test[index * 3 + 2]">{{ test[index * 3 + 2] }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
        wortcontainer: {
            a: ["auf", "an", "Au", "am", "au", "Auto", "al","Auge" ,"Moin"],
            b: ["bo", "Boden", "Be", "Bild", "baden", "Bi", "bu","bis" ,"Berge" ,"Bach" ,"Burg" ,"Blume" ,"Bus" ,"besuchen" ,"Buch" ,"Bauch" ,"Birne" ,"Brigitte"],
            c: ["Cola", "Cordular", "Copilot", "Crosslauf", "Carl", "China", "Clown", "Cobra", "clever"],
            d: ["dam", "Didi", "die", "da", "der", "das", "di","Dose" ,"Do" ,"Dame" ,"Drache" ,"del" ,"Dusche" ,"Dodo" ,"du" ,"De" ,"Dach" ,"dünn"],
            e: ["elf", "el", "Elefant", "Elf", "Elbe", "Erde", "Esel","essen" ,"Eber" ,"erst", "Emiel", "Elektro"],
            f: ["Fifa", "Felu", "Fimo", "fo", "Fa", "Filme", "Fla","Frau" ,"fi" ,"fragen" ,"Feuer" ,"fe" ,"Fächer","Flügel","Fridolin"],
            g: ["gi", "gut", "grau", "ge", "Geige", "Gabel", "Ga","Gäste" ,"Glück" ,"Gemüse" ,"gross", "Glocke"],
            h: ["holen", "Ho", "halt", "Hut", "Hi", "helfen", "hu","Haus" ,"Ha" ,"He" ,"Hose" ,"Hase","Hildegard", "Heu", "heulen"],
            i: ["Igel", "Ida", "im", "ins", "Insel", "ist", "Inge", "Iltis", "immer"],
            j: ["Junge", "Januar", "Jaguar", "Juli", "ja", "Jahr", "Jacke", "jetzt" ,"Jo-Jo" ,"jubeln" ,"Jäger", "Joy"],
            k: ["Knochen", "Klei", "Koko", "Kuchen", "Kiki", "kann", "kro","Kino" ,"Kajak" ,"kei" ,"kein" ,"Kamel" ,"Ku" ,"Kuh" ,"Koch" ,"Klasse" ,"Käfer" ,"Käse" ,
                "Käfig" ,"Kälte" ,"Küken"],
            l: ["lachen", "Lara", "Lilo", "Limo", "laufen", "Li", "Leo" ,"lo" ,"Lulu" ,"laut" ,"Lira" ,"la" ,"lila" ,"lu" ,"le" ,"Laus" ,"li" ,"Le" ,
                "Lose" ,"Lama" ,"Lärm" ,],
            m: ["Me", "Mo", "mi", "Mama", "ma", "Momo","Mimi" ,"mi" ,"Musik" ,"Mimo" ,"Ma" ,"mo" ,"ma" ,"Mu" ,"Moni" ,"me" ,"Maus" ,"Mauer" ,"Mumi" ,"machen" ,"Mari" ,
                "Mädchen" ,"Mütze" ,"Müll"],
            n: ["nasch", "Nagel", "nu", "Nala", "no", "ni", "Name","Nina" ,"na" ,"Ne" ,"Nase" ,"nanu"],
            o: ["Ofe", "Omi", "Oma", "Opa", "Onkel", "Ort", "Ofen", "Otto", "Olaf"],
            p: ["Paul", "Peter", "parken", "Pilz", "pa", "Papa", "Popel", "Person", "Paul"],
            q: ["Qualle", "qualm", "quer", "Quark", "quit", "quatsch", "Quader", "Quiz", "Quelle"],
            r: ["Rehe", "Roma", "Ria", "rau", "Ru", "raufen", "Re","ri" ,"Raum" ,"Ri" ,"Ruhe" ,"ra" ,"Rad" ,"Rabe" ,"ro" ,"Rasen" ,"rot" ,"Regen"],
            s: ["si", "Sala", "se", "Sofa", "su", "Sisi", "suchen","So" ,"sa" ,"sauer" ,"Se" ,"Sa" ,"Säge", "sauber", "sechs"],
            sch: ["sche", "scha", "Schere", "schon", "schu", "Scho", "Schal","Schlauch" ,"Schuh" ,"Schi" ,"Schlüssel", "Schule"],
            st: ["Stern", "Stier", "Star", "stolpern", "steif", "stossen", "Stab", "Stiel", "steuern"],
            t: ["Tara", "Tasche", "Tisch", "Tuch", "tauchen", "Traum", "Tiger","Tau" ,"Tür"],
            u: ["Uhu", "unu", "um", "Uwe", "Ufo", "Udo", "und","Ursular", "Uhr"],
            v: ["", "", "", "", "", "", ""],
            w: ["Wu", "Wa", "Willi", "wasch", "Wito", "Wo", "wo","wer" ,"was" ,"Wal" ,"wi" ,"we" ,"Wasser" ,"Wäsche" , "Wirbel",],
            x: ["", "", "", "", "", "", ""],
            y: ["", "", "", "", "", "", ""],
            z: ["zeigen", "Zeiger", "Zeit", "Zitrone", "Zettel", "Zoll", "Zoo", "Zebra", "Zelt",],
            ü: ["üben", "über", "Überaschung", "Übung", "Überfall", "übel", "Überfluss", "Übernahme", "Übersicht"],
            ö: ["", "", "", "", "", "", ""],
            ä: ["", "", "", "", "", "", ""],
            ei: ["Ei", "Eis", "Eisen", "Einfall", "Eiche", "eins", "einzeln","Eisbär", "Eisvogel"],
            eu: ["Euro", "Eule", "Europa", "euch", "Euter", "euer", "Eutin", "Euler", "Eurostar",],
        },
        test: ''

    };
  },
    methods: {
      ausgabeTeppich(value) {
        this.test = this.wortcontainer[value];
        },
    } 
}
</script>

<style scoped>
.navbar {
  background-color: lightgrey;
  margin-bottom: 1%;
  text-align: center;
  padding: 1%;
}

.navbar-brand {
    font-size: 25px;
    font-family: Ubuntu;
}
table {
  min-width: 700px;
}
  td {
      border: 3px solid;
      font-size: 35px;
      text-align: center;
      padding: 2%;
  }
  tr {
      padding: 2%; 
  }
  .tabellenformat {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 2%;

  }

</style>
