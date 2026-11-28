import { copyFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const output = new URL('../dist/', import.meta.url);
await mkdir(output, { recursive: true });
await copyFile(
  new URL('../demo/index.html', import.meta.url),
  new URL('index.html', output),
);
console.log(`Static demo assembled in ${fileURLToPath(output)}`);
