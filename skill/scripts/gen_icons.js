/**
 * Generate Material-style icons in Premier Cloud brand colors for pptxgenjs decks.
 * pptxgenjs has no icon library, so we render react-icons (Material Design) to SVG,
 * bake the color, and rasterize to PNG with sharp.
 *
 * Output: icons/<name>_<COLOR>.png  (256x256)  for COLOR in FFFFFF, 1E66AB, 38B4E7
 * Reference an icon in the deck as:  icons/cloud_1E66AB.png
 *
 * Run:  NODE_PATH=$(npm root -g) node gen_icons.js
 * Requires (global):  npm install -g react-icons react react-dom sharp
 *
 * Add/remove entries in `map` as a deck needs. Names are yours; components are the
 * Material (Md*) exports from react-icons/md.
 */
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const md = require("react-icons/md");
const sharp = require("sharp");
const fs = require("fs");

const map = {
  // general
  cloud: "MdCloud", cloudq: "MdCloudQueue", server: "MdDns", data: "MdStorage",
  check: "MdCheckCircle", star: "MdStars", rocket: "MdRocketLaunch", bolt: "MdBolt",
  growth: "MdTrendingUp", calendar: "MdEventAvailable", list: "MdChecklist",
  // people / partner
  groups: "MdGroups", handshake: "MdHandshake", contacts: "MdContacts",
  support: "MdSupportAgent", badge: "MdWorkspacePremium",
  // product / tech
  ai: "MdAutoAwesome", gemini: "MdAutoAwesome", api: "MdApi", migration: "MdSyncAlt",
  security: "MdShield", shieldcheck: "MdVerifiedUser", bug: "MdBugReport",
  hardware: "MdDevices", workspace: "MdGridView", code: "MdCode", video: "MdPlayCircle",
  appsheet: "MdAppShortcut", phone: "MdCall", funding: "MdAccountBalance",
  savings: "MdSavings", backup: "MdBackup", infra: "MdDns", swap: "MdSwapHoriz",
  layers: "MdLayers", settings: "MdSettings", build: "MdBuild",
};
const colors = { FFFFFF: "#FFFFFF", "1E66AB": "#1E66AB", "38B4E7": "#38B4E7" };

const OUT = "icons";
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  let n = 0;
  for (const [name, comp] of Object.entries(map)) {
    const Icon = md[comp];
    if (!Icon) { console.log("MISSING react-icons/md export:", comp); continue; }
    for (const [key, hex] of Object.entries(colors)) {
      const svg = renderToStaticMarkup(React.createElement(Icon, { size: 256 }))
        .replace(/currentColor/g, hex);
      await sharp(Buffer.from(svg)).resize(256, 256).png().toFile(`${OUT}/${name}_${key}.png`);
      n++;
    }
  }
  console.log("icons written:", n);
})();
