export async function fetchAllCards() {
  const res = await fetch("/cards");
  return await res.json();
}
