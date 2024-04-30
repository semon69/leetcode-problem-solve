const getProfit = (prices) => {
  let minPrice = prices[0]
  let maxProfit = 0

  for(let i = 1; i < prices.length; i++){
      minPrice = Math.min(minPrice, prices[i])
      maxProfit = Math.max(maxProfit, prices[i] - minPrice)
  }
  return maxProfit
//   let maxProfit = 0;
//   for (let i = 0; i < price.length; i++) {
//     for (let j = i + 1; j < price.length; j++) {
//       let profit = price[j] - price[i];
//       if (profit > maxProfit) {
//         maxProfit = profit;
//       }
//     }
//   }
//   return maxProfit;
};
// getProfit([7,1,5,3,6,4])
console.log(getProfit([7, 1, 5, 3, 6, 4]));
