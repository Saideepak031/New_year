from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Goal, Wish
from .forms import NoteForm, GoalForm, WishForm

def index(request):
    # handle forms
    if request.method == 'POST':
        if 'add_note' in request.POST:
            nf = NoteForm(request.POST)
            if nf.is_valid():
                nf.save()
                return redirect('newyear:index')
        if 'add_goal' in request.POST:
            gf = GoalForm(request.POST)
            if gf.is_valid():
                gf.save()
                return redirect('newyear:index')
        if 'add_wish' in request.POST:
            wf = WishForm(request.POST)
            if wf.is_valid():
                wf.save()
                return redirect('newyear:index')

    notes = Note.objects.order_by('-created')[:20]
    goals = Goal.objects.order_by('-created')[:20]
    wishes = Wish.objects.order_by('-created')[:50]

    context = {
        'notes': notes,
        'goals': goals,
        'wishes': wishes,
        'note_form': NoteForm(),
        'goal_form': GoalForm(),
        'wish_form': WishForm(),
    }
    return render(request, 'newyear/index.html', context)

# small actions

def delete_note(request, pk):
    n = get_object_or_404(Note, pk=pk)
    n.delete()
    return redirect('newyear:index')

def toggle_goal(request, pk):
    g = get_object_or_404(Goal, pk=pk)
    g.is_done = not g.is_done
    g.save()
    return redirect('newyear:index')
