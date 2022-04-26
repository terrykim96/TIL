/*
	[배열 관련 주요 메서드 연습 1]
	
	주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만드세요.
*/

const homeworks = ['david.zip', null, 'maria.zip', 'tom.zip', null]

const cleanedHomeworks = homeworks.filter((homework) => {
	return homework !== null
});

/*
	[배열 관련 주요 메서드 연습 2]
	
	주어진 배열을 사용하여 아래 문자열을 완성하세요.

	'www.samsung.com/sec/buds/galaxy-buds-pro'

*/

const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']

const arrs = [arr1, arr3, arr2];
const separators = ['.', '/', '-'];
const SEPARATOR = '/';

const url = arrs.map((arr, index) => {
	return arr.join(separators[index])
}).reduce((acc, element) => {
	return acc + SEPARATOR + element
});

/*
	[배열 관련 주요 메서드 연습 3]

	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']

const beforeWord = 'rainy';
const afterWord = 'sunny';

while (weather.indexOf(beforeWord) !== -1) {
	let index = weather.indexOf(beforeWord)
	weather[index] = afterWord
};