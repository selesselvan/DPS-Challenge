const hotpTotpGenerator = require('hotp-totp-generator');

console.log(hotpTotpGenerator.totp({
	key: "selesselvan@gmail.comDPSCHALLENGE",
	X: 120,
	T0: 0,
	algorithm: "sha512",
    digits: 10
}))