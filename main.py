import tokenizer
import spec
from spec import * 
from pyspec import _MethodWrap

#pyspec module should find all classes and apply this shitty bootstrap

klass = [Bow]
klass[0].score = _MethodWrap(klass[0], klass[0].score)

## unit test 

bowling = Bowling()
bowling.should_score_0_for_gutter_game()

