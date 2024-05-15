main();

function answerQueries(nums, queries, limit) {
  let prefix = [];
  prefix.push(nums[0]);
  for (let i = 1; i < nums.length; i++) {
    prefix.push(nums[i] + prefix[i - 1]);
  }

  let ans = [];

  queries.forEach((element) => {
    ans.push(prefix[element[1]] - prefix[element[0]] + nums[element[0]] < 13);
  });

  return ans;
}

function main() {
  let nums = [1, 6, 3, 2, 7, 2];
  let queries = [
    [0, 3],
    [2, 5],
    [2, 4],
  ];
  let limit = 13;

  console.log(answerQueries(nums, queries, limit));
}
