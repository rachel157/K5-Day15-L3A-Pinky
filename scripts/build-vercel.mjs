import { copyFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const output = new URL('../dist/', import.meta.url);
const assetsOutput = new URL('../dist/assets/', import.meta.url);
await mkdir(output, { recursive: true });
await mkdir(assetsOutput, { recursive: true });
await copyFile(
  new URL('../demo/index.html', import.meta.url),
  new URL('index.html', output),
);
const videoSource = new URL('../demo/assets/agent-video-internal-demo.mp4', import.meta.url);
if (existsSync(videoSource)) {
  await copyFile(
    videoSource,
    new URL('agent-video-internal-demo.mp4', assetsOutput),
  );
}
console.log(`Static demo assembled in ${fileURLToPath(output)}`);
