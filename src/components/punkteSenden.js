import axios from "axios";

export async function punkteSenden(punkte) {
  try {
    const response = await axios.post('http://127.0.0.1:5000/add_points', {
      punkte: punkte,
      user_id: 3,
    });
    console.log(response.data.message + " Frontend");
    console.log("Was ein Scheiß " + punkte);
  } catch (error) {
    console.error("Fehler beim Senden der Punkte: ", error);
  }
}








