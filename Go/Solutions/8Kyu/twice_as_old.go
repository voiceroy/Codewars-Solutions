package kata

func TwiceAsOld(dadYearsOld, sonYearsOld int) int {
	ageDifference := dadYearsOld - sonYearsOld
	if ageDifference > sonYearsOld { // The son is very young compared to father, so father must be twice his age some years ago
		return dadYearsOld - (sonYearsOld * 2)
	}
	return (sonYearsOld * 2) - dadYearsOld // The son is not very young compared to father, so father must be twice his age some years after
}
