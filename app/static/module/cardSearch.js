import { fetchAllCards } from "./apiClient.js";
import { resolveImage } from "./imageResolver.js";

let allCards = [];

const container = document.getElementById("card-container");
const searchInput = document.getElementById("search");

function normalize(text) {
  return text.toLowerCase();
}

function render(cards) {
  container.innerHTML = "";

  cards.forEach(card => {
    const div = document.createElement("div");
    div.className = "card";

    const img = document.createElement("img");
    img.src = resolveImage(card);
    
    img.onerror = () => {
      img.src = "/static/assets/placeholder.webp";
    };

    const title = document.createElement("div");
    title.className = "card-title";
    title.textContent = card.name;

    const code = document.createElement("div");
    code.className = "card-code";
    code.textContent = card.card_number;

    div.appendChild(img);
    div.appendChild(title);
    div.appendChild(code);

    container.appendChild(div);
  });
}

function filterCards(keyword) {
  const key = normalize(keyword);

  return allCards.filter(card =>
    normalize(card.name).includes(key) ||
    normalize(card.card_number).includes(key)
  );
}

(async function init() {
  allCards = await fetchAllCards();
  render(allCards);

  searchInput.addEventListener("input", e => {
    const value = e.target.value.trim();
    if (!value) {
      render(allCards);
    } else {
      render(filterCards(value));
    }
  });
})();
