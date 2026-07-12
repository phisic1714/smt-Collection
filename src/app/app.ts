import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import gamesList from './util/gameslist.json';
import { nanoid } from 'nanoid';
async function runGameFile(params: unknown) {
  await fetch('/api/run-game', {
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
  // imports: [RouterOutlet],
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
      window.open(`smtlauncher://launch?id=${val.run}`);
      // start  "C:\Users\pee\Desktop\duckstation-qt-x64-ReleaseLTCG - Shortcut.lnk" "C:\Program Files\Emulator\duckstation-windows-x64-release\game\Silent Hill (USA).bin"
      // exec('echo "The \\$HOME variable is $HOME"');
      // runGameFile(val);
    }
  }
  onGetFile(event: any) {
    console.log('event :>> ', event);
  }
}
