module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'header-max-length': [2, 'always', 72],
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'build',
        'ci',
        'chore',
        'revert'
      ]
    ],
    'subject-case': [2, 'always', ['sentence-case', 'start-case', 'lower-case']],
    'scope-case': [2, 'always', 'kebab-case'],
    'body-leading-blank': [2, 'always'],
    'footer-leading-blank': [1, 'always']
  }
};