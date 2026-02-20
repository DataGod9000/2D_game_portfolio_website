import { defineConfig } from "vite";

export default defineConfig({
  base: "/josephland/",
  build: {
    minify: "terser",
  },
});
