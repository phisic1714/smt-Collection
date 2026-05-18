import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import gamesList from './util/gameslist.json';

async function runGameFile(params: unknown) {
  await fetch('http://127.0.0.1:8000/run-game', {
    method: 'POST',
    body: JSON.stringify(params),
    headers: {
      'Content-Type': 'application/json',
    },
    // …
  });
}
@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  title = signal('ควย');
  games = signal(gamesList);

  onPress(val: { name: string; platform: string; image: string; run: string }) {
    console.log('val :>> ', val);
    if (['Steam'].includes(val.platform)) {
      window.open(`steam://rungameid/${val.run}`);
    } else {
      // start  "C:\Users\pee\Desktop\duckstation-qt-x64-ReleaseLTCG - Shortcut.lnk" "C:\Program Files\Emulator\duckstation-windows-x64-release\game\Silent Hill (USA).bin"
      // exec('echo "The \\$HOME variable is $HOME"');
      runGameFile(val);
    }
  }
}
