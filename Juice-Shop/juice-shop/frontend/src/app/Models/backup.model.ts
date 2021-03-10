/*
 * Copyright (c) 2014-2021 Bjoern Kimminich.
 * SPDX-License-Identifier: MIT
 */

export interface Backup {
  version: number
  continueCode?: string
  language?: string
  banners?: { welcomeBannerStatus?: string, cookieConsentStatus?: string }
  scoreBoard?: { showOnlyTutorialChallenges?: boolean, displayedChallengeCategories?: string[], displayedDifficulties?: number[], showDisabledChallenges?: boolean, showSolvedChallenges?: boolean }
}
